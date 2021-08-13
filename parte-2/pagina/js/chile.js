let regiones_dic = {
    "Región de Tarapacá": ['Camiña','Huara','Pozo Almonte','Iquique','Pica','Colchane','Alto Hospicio'],
    "Región de Antofagasta": ['Tocopilla','Maria Elena','Ollague','Calama','San Pedro Atacama','Sierra Gorda','Mejillones','Antofagasta','Taltal'],
    "Región de Atacama": ['Diego de Almagro','Chañaral','Caldera','Copiapo','Tierra Amarilla','Huasco','Freirina','Vallenar','Alto del Carmen'],
    "Región de Coquimbo": ['La Higuera','La Serena','Vicuña','Paihuano','Coquimbo','Andacollo','Rio Hurtado','Ovalle','Monte Patria','Punitaqui','Combarbala','Mincha','Illapel','Salamanca','Los Vilos'],
    "Región de Valparaíso": ['Petorca','Cabildo','Papudo','La Ligua','Zapallar','Putaendo','Santa Maria','San Felipe','Pencahue','Catemu','Llay Llay','Nogales','La Calera','Hijuelas','La Cruz','Quillota','Olmue','Limache','Los Andes','Rinconada','Calle Larga','San Esteban','Puchuncavi','Quintero','Viña del Mar','Villa Alemana','Quilpue','Valparaiso','Juan Fernandez','Casablanca','Concon','Isla de Pascua','Algarrobo','El Quisco','El Tabo','Cartagena','San Antonio','Santo Domingo'],
    "Región del Libertador Bernardo Ohiggins": ['Mostazal','Codegua','Graneros','Machali','Rancagua','Olivar','Doñihue','Requinoa','Coinco','Coltauco','Quinta Tilcoco','Las Cabras','Rengo','Peumo','Pichidegua','Malloa','San Vicente','Navidad','La Estrella','Marchigue','Pichilemu','Litueche','Paredones','San Fernando','Peralillo','Placilla','Chimbarongo','Palmilla','Nancagua','Santa Cruz','Pumanque','Chepica','Lolol'],
    "Región del Maule": ['Teno','Romeral','Rauco','Curico','Sagrada Familia','Hualañe','Vichuquen','Molina','Licanten','Rio Claro','Curepto','Pelarco','Talca','Pencahue','San Clemente','Constitucion','Maule','Empedrado','San Rafael','San Javier','Colbun','Villa Alegre','Yerbas Buenas','Linares','Longavi','Retiro','Parral','Chanco','Pelluhue','Cauquenes'],
    "Región del Biobío": ['Tome','Florida','Penco','Talcahuano','Concepcion','Hualqui','Coronel','Lota','Santa Juana','Chiguayante','San Pedro de la Paz','Hualpen','Cabrero','Yumbel','Tucapel','Antuco','San Rosendo','Laja','Quilleco','Los Angeles','Nacimiento','Negrete','Santa Barbara','Quilaco','Mulchen','Alto Bio Bio','Arauco','Curanilahue','Los Alamos','Lebu','Cañete','Contulmo','Tirua'],
    "Región de La Araucanía": ['Renaico','Angol','Collipulli','Los Sauces','Puren','Ercilla','Lumaco','Victoria','Traiguen','Curacautin','Lonquimay','Perquenco','Galvarino','Lautaro','Vilcun','Temuco','Carahue','Melipeuco','Nueva Imperial','Puerto Saavedra','Cunco','Freire','Pitrufquen','Teodoro Schmidt','Gorbea','Pucon','Villarrica','Tolten','Curarrehue','Loncoche','Padre Las Casas','Cholchol'],
    "Región de Los Lagos": ['San Pablo','San Juan','Osorno','Puyehue','Rio Negro','Purranque','Puerto Octay','Frutillar','Fresia','Llanquihue','Puerto Varas','Los Muermos','Puerto Montt','Maullin','Calbuco','Cochamo','Ancud','Quemchi','Dalcahue','Curaco de Velez','Castro','Chonchi','Queilen','Quellon','Quinchao','Puqueldon','Chaiten','Futaleufu','Palena','Hualaihue'],
    "Región Aisén del General Carlos Ibáñez del Campo": ['Guaitecas','Cisnes','Aysen','Coyhaique','Lago Verde','Rio Ibañez','Chile Chico','Cochrane','Tortel',"O'Higins"],
    "Región de Magallanes y la Antártica Chilena": ['Torres del Paine','Puerto Natales','Laguna Blanca','San Gregorio','Rio Verde','Punta Arenas','Porvenir','Primavera','Timaukel','Antartica'],
    "Región Metropolitana de Santiago": ['Tiltil','Colina','Lampa','Conchali','Quilicura','Renca','Las Condes','Pudahuel','Quinta Normal','Providencia','Santiago','La Reina','Ñuñoa','San Miguel','Maipu','La Cisterna','La Florida','La Granja','Independencia','Huechuraba','Recoleta','Vitacura','Lo Barrenechea','Macul','Peñalolen','San Joaquin','La Pintana','San Ramon','El Bosque','Pedro Aguirre Cerda','Lo Espejo','Estacion Central','Cerrillos','Lo Prado','Cerro Navia','San Jose de Maipo','Puente Alto','Pirque','San Bernardo','Calera de Tango','Buin','Paine','Peñaflor','Talagante','El Monte','Isla de Maipo','Curacavi','Maria Pinto','Melipilla','San Pedro','Alhue','Padre Hurtado'],
    "Región de Los Ríos": ['Lanco','Mariquina','Panguipulli','Mafil','Valdivia','Los Lagos','Corral','Paillaco','Futrono','Lago Ranco','La Union','Rio Bueno'],
    "Región Arica y Parinacota": ['Gral. Lagos','Putre','Arica','Camarones'],
    "Región del Ñuble": ['Cobquecura','Ñiquen','San Fabian','San Carlos','Quirihue','Ninhue','Trehuaco','San Nicolas','Coihueco','Chillan','Portezuelo','Pinto','Coelemu','Bulnes','San Ignacio','Ranquil','Quillon','El Carmen','Pemuco','Yungay','Chillan Viejo']
};

let list = Object.keys(regiones_dic)
let large = list.length;
let regiones = document.getElementById("region");

function region(){
	for (let i = 0; i < large; i++){
		let option = document.createElement("option");
		option.text = list[i]
		regiones.add(option);
	}
}

function comunas(){
	let region_actual = regiones.value;
	let comunas = document.getElementById("comuna");
	comunas.innerHTML = '';

	for (let i = 0; i < large; i++){
		if(region_actual == list[i]){
			let list2 = regiones_dic[list[i]]
			let large2 = list2.length;
			for(let j = 0; j < large2; j++){
				let option = document.createElement("option");
				option.text = list2[j];
				comunas.add(option);
			}
		}
	}
}

region();
comunas();

