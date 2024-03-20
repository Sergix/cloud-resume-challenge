var baseURL = "https://b7o3qabiij.execute-api.us-east-1.amazonaws.com/Prod"

document.addEventListener("DOMContentLoaded", function(event) {
	var xhr = new XMLHttpRequest({ mozSystem: true, mozAnon: true });
	xhr.onreadystatechange = function() {
		if (this.readyState === 4 && this.status === 200) {
			document.getElementById("visitor-counter").innerHTML = "Visitors: " + this.responseText;
		}
	};
	xhr.open("GET", baseURL + "/visitor-count?action=increment", true);

	// secret flag for disabling
	if (window.location.hash !== "#nojs") {
		xhr.send();
	}
})
