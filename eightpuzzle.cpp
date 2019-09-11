// Reference Links
// https://www.geeksforgeeks.org/priority-queue-in-cpp-stl/
// https://blog.goodaudience.com/solving-8-puzzle-using-a-algorithm-7b509c331288

#include<bits/stdc++.h>
using namespace std;
struct node{
	int board[3][3], cost,g;
	int x,y; //coordinates of blank tile
	node* parent;
};

int row[] = { 1, 0, -1, 0 }; 
int col[] = { 0, -1, 0, 1 }; //all 4 movement of a tile

int hamming(int ar[3][3])
{   
	int i,j,count=1,h=0;
	for (i=0;i<3;i++){
		for(j=0;j<3;j++){
			if(i+j!=4 && count!=ar[i][j])
				h++;
			count++;
		}
	}
	return h;
}

//to get new state
node* nState(int mat[3][3], int xi, int yi, int xf, int yf, int g, node* parent) 
{ 
    node* n = new node; 
    n->parent = parent; 
  
    memcpy(n->board, mat, sizeof(n->board)); 
    //slide tile by 1 position 
    swap(n->board[xi][yi], n->board[xf][yf]); 
  
    n->cost = INT_MAX; 
  
    //set number of moves so far 
    n->g = g; 

    n->x = xf; 
    n->y = yf; 
    return n; 
} 

void printbrd(int ar[3][3]){
	int i,j;
	for(i=0;i<3;i++){
		for(j=0;j<3;j++){
			if(ar[i][j]!=0)
				cout<<ar[i][j]<<" ";
			else
				cout<<"  ";
		}
		cout<<endl;
	}
}

//recursion to print the sequence
void printPath(node* root) 
{ 
    if (root == NULL) 
        return; 
    printPath(root->parent); 
    printbrd(root->board);
    cout<<"g : "<<root->g<<"   "<<" h : "<<root->cost<<"   "<<"Cost : "<<root->g+root->cost<<endl;
    cout<<endl; 
} 

struct calcf 
{ 
    bool operator()(const node* m, const node* n) const
    { 
    	//f=g+h
        return (m->cost + m->g) > (n->cost + n->g); 
    } 
}; 

int valid(int x, int y) 
{ 
    return (x>=0 && x<3 && y>=0 && y<3); 
} 

int main(){
	
	int board[3][3]={{1,2,3},{0,4,6},{7,5,8}};
	int x=1,y=0; // position of the blank
	cout<<"Parent : "<<endl<<endl;
	printbrd(board);
	
	priority_queue<node*, vector<node*>, calcf> explore;
	
	node* root = nState(board, x, y, x, y, 0, NULL); 
    root->cost = hamming(board); 
	explore.push(root); 
    int iter=0;
    while (!explore.empty())
	{
		/*
    	cout<<"Iteration #"<<iter<<endl;
    	iter++;
    	if (iter==11)
    		break
    	*/
    	
    	node* min = explore.top(); 
        explore.pop(); 
       
        if (min->cost == 0) 
        { 
            cout<<"Path : "<<endl<<endl<<endl;
            printPath(min); 
            break; 
        } 
  
        
        // min is the node popped from the priority queue
        cout<<"Children at level  :"<<iter<<endl<<endl<<endl;
        for (int i=0;i<4;i++) 
        { 
            if (valid(min->x+row[i], min->y+col[i])) 
            { 
                
                node* child = nState(min->board, min->x, min->y, min->x + row[i], min->y + col[i], min->g + 1, min); 
                child->cost = hamming(child->board);
                
            	printbrd(child->board);
            	
            	cout<<endl<<endl;
                explore.push(child); 
            } 
        } 
        iter++;
	}

	return 0;
}
