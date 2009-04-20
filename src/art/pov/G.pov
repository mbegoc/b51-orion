//etoile de type G
//temperature 5 200 a 6 000K
//taille 0.96 a 1.15 r_soleil
//7.6% des etoiles sur leur sequence primaire


#include "colors.inc"
#include "etoiles.inc"
#include "finish.inc"


#declare Etoile = sphere
{
  <0, 0, 0>, 1.0
  
  texture
  {
    pigment { color couleurG }
  }
  
  normal 
  { 
    bumps 0.8 
    scale 0.1 //a changer selon la taille de l'etoile: plus petit pour petite etoile
  }
  
  finish 
  {
    
    ambient 0.6
    //reflection 0.2
    //specular 0.1
    //roughness 0.2
  
  } 
}

Etoile

camera
{
  location d_camera
  look_at  <0, 0, 0>
}


light_source
{
  <0 , 20, -30>
  color White
  cylinder
  radius 10
  falloff 10
  tightness 0
  point_at <0, 0, 0>
}

/*
fog 
{
    distance 20
    color rgbf<0.62,0.75,1.0,0.5>
} 
*/




