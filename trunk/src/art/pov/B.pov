//etoile de type B
//temperature 10 000 a 30 000K
//taille 1.8 a 6.6 r_soleil
//0.13% des etoiles sur leur sequence primaire


#include "colors.inc"
#include "etoiles.inc"
#include "finish.inc"


#declare Etoile = sphere
{
  <0, 0, 0>, 3
  
  texture
  {
    pigment { color couleurB }
  }
  
  normal 
  { 
    bumps 0.8 
    scale 0.4 //a changer selon la taille de l'etoile: plus petit pour petite etoile
  }
  
  finish 
  {
    
    ambient 1.0
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




