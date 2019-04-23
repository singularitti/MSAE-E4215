#!/usr/bin/env wolframscript
(* ::Package:: *)

(* ::Input:: *)
(*Clear["Global`*"];*)
(*\[Sigma][t_]:=\[Sigma]0 UnitStep[t];*)
(*solByMMA=Assuming[t>0,(e/.DSolve[{(Ea+Eb)e'[t]+Ea Eb/(3\[Eta])e[t]==\[Sigma]'[t]+Ea/(3\[Eta])\[Sigma][t],e[0]==e0},e,t][[1,1]])[t]]//FullSimplify*)
(*solByMe=(InverseLaplaceTransform[(CC \[Sigma]0/s+e0)/(A+s),s,t]//Simplify)/.{A->(Ea Eb/(Ea+Eb))/(3\[Eta]),CC->(Ea/(Ea+Eb))/(3\[Eta]),e0->e0}//FullSimplify*)
(*solByMMA-solByMe//FullSimplify*)



