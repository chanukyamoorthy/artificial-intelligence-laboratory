env(papers,verbal). %facts
env(documents,verbal).
env(manuals,verbal).
env(documents,verbal).
env(pictures,visual).
env(illustrations,visual).
env(photographs,visual).
env(diagrams,visual).
env(machines,physical_object).
env(buildings,physical_object).
env(tools,physical_object).
env(numbers,symbolic).
env(formulas,symbolic).
env(computer_programs,symbolic).
job(lecturing,oral).
job(advising,oral).
job(counselling,oral).
job(building,hands-on).
job(repairing,hands-on).
job(troubleshooting,hands-on).
job(writing,documented).
job(typing,documented).
job(drawing,documented).
job(evaluating,analytical).
job(reasoning,analytical).
job(investigating,analytical).
medium(physical_object,hands-on,required,workshop).
medium(symbolic,analytical,required,lecture-tutorial).
medium(visual,documented,not-required,videocassette).
medium(visual,oral,required,lecture-tutorial).
medium(verbal,analytical,required,lecture-tutorial).
medium(verbal,oral,required,role-play-exercises).


%function
med(X,Y,Z,W):-
    env(X,A), 
    job(Y,B), 
    medium(A,B,Z,W),
    write('The stimulus_situation is - '),write(A),nl,
    write('The stimulus_response is - '),write(B),nl,
    write('The feedback is - '),write(Z),nl,
    write('So the medium is - '),write(W).

