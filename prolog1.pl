verbal(papers).
verbal(manuals).
verbal(documents).
verbal(textbooks).

visual(pictures).
visual(illustrations).
visual(photographs).
visual(diagrams).

phy(machines).
phy(buildings).
phy(tools).

sym(numbers).
sym(formulas).
sym('computer_programs').

oral(lecturing).
oral(advising).
oral(counselling).

hands_on(building).
hands_on(repairing).
hands_on(troubleshooting).

doc(writing).
doc(typing).
doc(drawing).

analytical(evaluating).
analytical(reasoning).
analytical(investigating).

feedback(required).

workshop(X,Y,Z) :- phy(X),hands_on(Y),feedback(Z).
video_cassette(X,Y,Z) :- visual(X),doc(Y),not(feedback(Z)).
lecture_tutorial(X,Y,Z) :- sym(X),analytical(Y),feedback(Z).
lecture_tutorial(X,Y,Z):- visual(X),oral(Y),feedback(Z).
lecture_tutorial(X,Y,Z):- verbal(X),analytical(Y),feedback(Z).
roleplay_exercises(X,Y,Z):- verbal(X),oral(Y),feedback(Z).

hands_on_display(X):-(hands_on(X)->writeln('hands_on')).
medium(X,Y,Z):-(workshop(X,Y,Z)->writeln('workshop')).
medium(X,Y,Z):-(lecture_tutorial(X,Y,Z)->writeln('lecture tutorial')).
medium(X,Y,Z):-(video_cassette(X,Y,Z)->writeln('video cassette')).
medium(X,Y,Z):-(roleplay_exercises(X,Y,Z)->writeln('role play exercises')).
