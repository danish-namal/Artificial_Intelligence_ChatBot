mian_of(chotekhan,chotirani).
mian_of(barrekhan,barrirani).
mian_of(salim,kausar).
mian_of(nadir,nahid).
mian_of(asad,sumra).
mian_of(rizwan,sanam).



parent_of(chotekhan,kausar).
parent_of(chotirani,kausar).
parent_of(chotekhan,nadir).
parent_of(chotirani,nadir).
parent_of(chotekhan,asad).
parent_of(chotirani,asad).
parent_of(barrekhan,nahid).
parent_of(barrirani,nahid).
parent_of(barrekhan,sumra).
parent_of(barrirani,sumra).
parent_of(salim,rizwan).
parent_of(kausar,rizwan).
parent_of(nadir,burhan).
parent_of(nahid,burhan).
parent_of(nadir,rashid).
parent_of(nahid,rashid).
parent_of(nadir,akram).
parent_of(nahid,akram).
parent_of(asad,salima).
parent_of(sumra,salima).
parent_of(asad,sanam).
parent_of(sumra,sanam).
parent_of(rizwan,rabia).
parent_of(sanam,rabia).




gins(mard,chotekhan).
gins(mard,barrekhan).
gins(mard,salim).
gins(mard,nadir).
gins(mard,asad).
gins(mard,rizwan).
gins(mard,burhan).
gins(mard,rashid).
gins(mard,akram).



gins(aurat,chotirani).
gins(aurat,barrirani).
gins(aurat,kausar).
gins(aurat,nahid).
gins(aurat,sumra).
gins(aurat,salima).
gins(aurat,sanam).
gins(aurat,rabia).





baap(V1,V2) :-parent_of(V1, V2),gins(mard, V1).

maa(V1,V2) :- parent_of(V1, V2), gins(aurat, V1).

beti(V1,V2):-parent_of(V2,V1) , gins(aurat,V1).

beta(V1,V2) :- parent_of(V2,V1), gins(mard,V1).

dada(V1,V2) :- parent_of(V1,Z) , parent_of(Z,V2) , gins(mard,V1),gins(mard,Z).

nana(V1,V2) :- parent_of(V1,Z), parent_of(Z,V2) , gins(mard,V1) , gins(aurat,Z).

dadi(V1,V2) :- parent_of(V1,Z),parent_of(Z,V2) , gins(aurat,V1), gins(mard,Z).

nani(V1,V2) :- parent_of(V1,Z),parent_of(Z,V2) , gins(aurat,V1), gins(aurat,Z).

sala(V1,V2) :- mian_of(V2,Z) , parent_of(A,Z) , gins(aurat,Z), parent_of(A,V1) , gins(mard,A), gins(mard,V1).

bahu(V1,V2) :- parent_of(V2,Z) , gins(aurat,V1) , gins(mard,Z) , mian_of(Z,V1).

pota(V1,V2) :- parent_of(V2,Z), parent_of(Z,V1) , gins(mard,V1),gins(mard,Z).

poti(V1,V2) :- parent_of(V2,Z), parent_of(Z,V1) , gins(aurat,V1),gins(mard,Z).


nawasa(V1,V2) :- parent_of(V2,Z), parent_of(Z,V1) , gins(mard,V1), gins(aurat,Z).

nawasi(V1,V2) :- parent_of(V2,Z), parent_of(Z,V1) , gins(aurat,V1), gins(aurat,Z).


sussar_h(V1,V2) :- mian_of(V2,Z) , parent_of(V1,Z) , gins(mard,V1), gins(aurat,Z), gins(mard,V2).

sussar_w(V1,V2) :- mian_of(Z,V2) , parent_of(V1,Z) , gins(mard,V1), gins(mard,Z), gins(aurat,V2).

bapdada(X,Y) :- parent_of(X,Y), gins(mard,X).
bapdada(X,Y) :- parent_of(X,Z) ,bapdada(Z,Y),gins(mard,Z),gins(mard,X).

khala(V1,V2):-parent_of(A,Z),parent_of(A,V1),parent_of(Z,V2),gins(aurat,V1),gins(aurat,Z),not(Z=V1).

chachataya(V1,V2):-parent_of(A,Z),parent_of(A,V1),parent_of(Z,V2),gins(mard,V1),gins(mard,Z),not(Z=V1).
