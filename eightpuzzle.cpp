#include<bits/stdc++.h>
using namespace std;

int goal[3][3] {{1,2,3},{4,5,6},{7,8,-1}};
 
struct node{
	int currentState[3][3];
	struct node *parent;
	int h;
	int f;	
};

struct compare_fscore{
	bool operator()(node const &p1, node const &p2)
	{
		return p2.f<p1.f;
	}
};

int calculate_hScore(int misplaced[3][3])
{
	int hScore=0;
	for(int i=0;i<3;i++)
	{
		for(int j=0;j<3;j++)
		{
			if(misplaced[i][j]!=-1 && misplaced[i][j]!=goal[i][j])
				hScore++;
		}
	}	
	return hScore;
}

struct node newNode(int newState[3][3], struct node *ptr, int height)
{
	struct node temp;
	for(int i=0;i<3;i++)
	{
		for(int j=0;j<3;j++)
		{
			temp.currentState[i][j]=newState[i][j];
		}
	}
	temp.parent=ptr;
	temp.h=height;
	temp.f=calculate_hScore(newState)+height;
	return temp;
}

/*
void recurse(struct node *root)
{
	if(root==NULL)
		return;
	recurse(root->parent);
	for(int j=0;j<3;j++)
	{
		for(int k=0;k<3;k++)
		{
			cout<<root->currentState[j][k]<<" ";
		}
		cout<<endl;
	}
	cout<<"g= "<<root->h<<", h= "<<root->f-root->h<<", f= "<<root->f<<endl;
	cout<<endl;
	
	
}

void printSolution(vector <node> closeList)
{
	struct node temp=closeList[closeList.size()-1];
	for(int j=0;j<3;j++)
	{
		for(int k=0;k<3;k++)
		{
			cout<<temp.currentState[j][k]<<" ";
		}
		cout<<endl;
	}
	struct node *ptr=&temp;
	recurse(ptr);	
	
}
*/

void printSolution(vector <node> closeList)
{
	for(int i=0;i<closeList.size();i++)
	{
		for(int j=0;j<3;j++)
		{
			for(int k=0;k<3;k++)
			{
				cout<<closeList[i].currentState[j][k]<<" ";
			}
			cout<<endl;
		}
		cout<<"g= "<<closeList[i].h<<", h= "<<closeList[i].f-closeList[i].h<<", f= "<<closeList[i].f<<endl;
		cout<<endl;
	}	
}


void solvePuzzle(int currentState[3][3])
{
	priority_queue<node,vector<node>,compare_fscore> openList;
	vector <node> closeList;
	openList.push(newNode(currentState,NULL,0));
	while(!openList.empty())
	{
		struct node optimal=openList.top();
		if(calculate_hScore(optimal.currentState)==0)
		{
			openList.pop();
			closeList.push_back(optimal);
			break;	
		}
		openList.pop();
		closeList.push_back(optimal);
		for(int i=0;i<3;i++)
		{
			for(int j=0;j<3;j++)
			{
				if(optimal.currentState[i][j]==-1)
				{
					//swap up
					if(i-1>=0)
					{
						swap(optimal.currentState[i][j],optimal.currentState[i-1][j]);
						openList.push(newNode(optimal.currentState,&optimal,optimal.h+1));	
						swap(optimal.currentState[i][j],optimal.currentState[i-1][j]);
					}
					//swap down
					if(i+1<3)
					{
						swap(optimal.currentState[i][j],optimal.currentState[i+1][j]);
						openList.push(newNode(optimal.currentState,&optimal,optimal.h+1));	
						swap(optimal.currentState[i][j],optimal.currentState[i+1][j]);
					}
					//swap left
					if(j-1>=0)
					{
						swap(optimal.currentState[i][j],optimal.currentState[i][j-1]);
						openList.push(newNode(optimal.currentState,&optimal,optimal.h+1));	
						swap(optimal.currentState[i][j],optimal.currentState[i][j-1]);
					}
					//swap right
					if(j+1<3)
					{
						swap(optimal.currentState[i][j],optimal.currentState[i][j+1]);
						openList.push(newNode(optimal.currentState,&optimal,optimal.h+1));	
						swap(optimal.currentState[i][j],optimal.currentState[i][j+1]);
					}
					
					break;
				}
			}
		}
		
	}
	printSolution(closeList);
}


int main()
{
	int currentState[3][3]={{1,2,3},{-1,4,6},{7,8,5}};
	solvePuzzle(currentState);
}

