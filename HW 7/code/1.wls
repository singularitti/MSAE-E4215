#!/usr/bin/env wolframscript
(* ::Package:: *)

Clear["Global`*"]
DSolve[{Eb e[t]+tau (Es+Eb) D[e[t],t]==sg0,e'[Infinity]==0},e,t]
DSolve[{tau D[sg[t],t]+sg[t]==sg0,sg'[0]==0},sg,t]
Plot[1-Exp[-t],{t,0,10},PlotRange->All]
