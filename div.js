function derouler(id_Div,id_Text)
{
	var div_cible;
	var text_plus_moins;
	div_cible = document.getElementById(id_Div) ;
	text_plus_moins=document.getElementById(id_Text);

	if (div_cible.style.display == "none")
		{
		div_cible.style.display = "" ;
		text_plus_moins.innerHTML="-";
		} 
	else {
		div_cible.style.display = "none" ;
		text_plus_moins.innerHTML="+";
		}
}

