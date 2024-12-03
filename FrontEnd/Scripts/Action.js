async function fetchData(url, elementId) {
	try {
			const response = await fetch(url);
			const data = await response.json();

			// Si la donnée est un tableau, on l'affiche sous forme de liste
			if (Array.isArray(data) && data.length > 0) 
			{
				document.getElementById(elementId).innerHTML = JSON.stringify(data, null, 2);
			} 
			else if (data.count !== undefined) 
			{
				// Si la donnée contient un champ "count", on l'affiche comme un nombre
				document.getElementById(elementId).innerHTML = `Nombre: ${data.count}`;
			} 
			else 
			{
				// Par défaut, on affiche le contenu JSON
				document.getElementById(elementId).innerHTML = JSON.stringify(data, null, 2);
			}
			
		} catch (error) 
		{
			document.getElementById(elementId).innerHTML = `Erreur lors de la récupération des données: ${error.message}`;
		}
}
