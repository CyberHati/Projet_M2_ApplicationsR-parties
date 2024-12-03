window.onload = function() {
	// Charger les différentes sections avec les bonnes URL de l' API
	fetchData("http://192.168.200.39:8000/Commercial/A", "commercial-a");
	fetchData("http://192.168.200.39:8000/Industriel/B", "industriel-b");
	fetchData("http://192.168.200.39:8000/Qualite/A", "qualite-a");
	fetchData("http://192.168.200.39:8000/RechercheEtDevloppement/A", "recherche-a");
	fetchData("http://192.168.200.39:8000/RessourcesHumaines/A", "ressources-a");
	fetchData("http://192.168.200.39:8000/Maintenance/B", "maintenance-b");
	fetchData("http://192.168.200.39:8000/AssistanceCommerciale/B", "assistance-b");
}