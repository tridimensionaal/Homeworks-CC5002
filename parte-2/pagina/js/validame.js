let bol = true;

function hasError(variable, max, regex, min=0){
	if (variable.length < min || variable.length > 100 || !regex.test(variable)){
		bol = false;
		return true;
	}
	return false;
}

function error_text(type, name){
	return type + " '" + name + "' no es válido. \n\n";
}

function validation() {
	bol = true;
    let error = "";

    let regiones = Object.keys(regiones_dic)

    //Validar región
    let actual_region = document.getElementsByName("region")[0].value;
    let bol_region = 0;
    let i_region = -1;
    for (let i = 0; i < regiones.length; i++){
        if (actual_region == regiones[i]){
            bol_region = 1;
            i_region = regiones[i];
            break;
        }
    }

    if(bol_region == 0){
        error += error_text("Region",  actual_region);
    }

    //Validar comuna
    let actual_comuna = document.getElementsByName("comuna")[0].value;
    if(bol_region == 0){
        error += error_text("Region",  actual_region);
    }
    else{
        let comunas = regiones_dic[i_region];
        if (comunas.indexOf(actual_comuna) == -1){
            error += error_text("Comuna", actual_comuna);
        }
    }

	//Validar sector
    let sector = document.getElementsByName("sector")[0].value; 
	let sector_regex = /^([A-zÁ-ú]+)((\s)([A-zÁ-ú]|[1-9])+)*$/

	if(sector.length!=0){
		if(hasError(sector,100,sector_regex)){
			error += error_text("Sector",sector);
		}
	}

	//Validar Nombre
    let nombre = document.getElementsByName("nombre")[0].value; 
	let nombre_regex = /(^([A-zÁ-ú]+)$)|(^([A-zÁ-ú]+)(\s)([A-zÁ-ú]+)$)|(^([A-zÁ-ú]+)(\s)([A-zÁ-ú]+)(\s)([A-zÁ-ú]+)$)|(^([A-zÁ-ú]+)(\s)([A-zÁ-ú]+)(\s)([A-zÁ-ú]+)(\s)([A-zÁ-ú]+)$)/;

	if(hasError(nombre,100,nombre_regex)){
		error += error_text("Nombre", nombre);
	}

	//Validar email 
	let email = document.getElementsByName("email")[0].value; 
    let email_regex = /^[A-z0-9]+([.\_][A-z0-9]+)*[@][a-z]+([.][a-z]+)+$/;
	if(hasError(email,100,email_regex)){
		error += error_text("Email", email);
	}

	//Validar numero de celular
	let number = document.getElementsByName("celular")[0].value; 
    if(number.length != 0){
        let number_regex = /^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{3,6}$/
        if(hasError(number,100,number_regex)){
            error += error_text("Numero", number);
        }
    }

	//Validar fechas de avistamientos
	let date = document.getElementsByName("dia-hora-avistamiento");
	let large = date.length;
	let date_regex =/^\d{4}\-\d{2}\-\d{2}\n\d{2}:\d{2}$/;

	for(let i = 0; i < large; i++){
		if(hasError(date[i].value,100, date_regex)){
			let num = i+1;
			error += error_text("Día-hora del avistamiento " + num, date[i].value);
		}
	}

    //Validar tipo
    let tipo = document.getElementsByName("tipo-avistamiento")
    let large_tipo = tipo.length;
    let tipos = ["Insecto", "Arácnido", "Miriápodo", "No sé"]
	for(let i = 0; i < large_tipo; i++){
        if (tipos.indexOf(tipo[i].value) == -1){
            let num = i + 1;
            bol = false;
            error += error_text("Tipo " + num, tipo[i].value);
        }
	}


    //Validar estados
    let estado = document.getElementsByName("estado-avistamiento");
    let large_estado = estado.length;
    let estados = ["Vivo", "Muerto", "No sé"];
	for(let i = 0; i < large_estado; i++){
        if (estados.indexOf(estado[i].value) == -1){
            let num = i + 1;
            bol = false;
            error += error_text("Estado " + num, estado[i].value);
        }
	}

    //Validar fotos
    let fotos = document.getElementsByName("foto-avistamiento");
    let large_fotos = fotos.length;
	let foto_regex = /\.(|jpe?g|png)$/;
	for(let i = 0; i < large_fotos; i++){
        let f = fotos[i].value;
        let ff = f.replace(/^.*[\\\/]/, '');
		if(hasError(ff, 100, foto_regex)){
			let num = i+1;
			error += error_text("Foto " + num, ff);
		}
	}

	error += "Ingrese los datos nuevamente";

	if(bol){
		return confirm("¿Esta seguro que desea enviar esta información?")
		//let form = document.getElementById("formulario");
		//form.innerHTML = "<h3> Hemos recibido su información, muchas gracias por colaborar</h3>";
	}
	else{
		alert(error);
		return false;
	}
}
