//etoile de type F
//temperature 6 000 a 7 500K
//taille 1.15 a 1.4 r_soleil
//3% des etoiles sur leur sequence primaire


#include "colors.inc"
#include "etoiles.inc"
#include "finish.inc"


#declare Etoile = sphere
{
  <0, 0, 0>, 1.2
  
  texture
  {
    pigment { color couleurF }
  }
  
  normal 
  { 
    bumps 0.8 
    scale 0.1 //a changer selon la taille de l'etoile: plus petit pour petite etoile
  }
  
  finish 
  {
    
    ambient 0.9
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
  radius 1
  falloff 10
  tightness 10
  point_at <0, 0, 0>
}

/*
fog 
{
    distance 20
    color rgbf<0.62,0.75,1.0,0.5>
} 
*/




