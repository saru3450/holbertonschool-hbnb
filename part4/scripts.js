/* 
This is a SAMPLE FILE to get you started.
Please, follow the project instructions to complete the tasks.
*/
document.addEventListener('DOMContentLoaded', () => {
  checkAuthentication();
});

document.addEventListener('DOMContentLoaded', () => {
  // On récupère le formulaire par son ID
  const loginForm = document.getElementById('login-form');

  // Si le formulaire existe
  if (loginForm) {
    // On écoute la soumission du formulaire
    loginForm.addEventListener('submit', async (event) => {
      // Empêche le rechargement automatique de la page
      event.preventDefault();

      // Récupère les valeurs des champs email et mot de passe
      const email = document.getElementById('email').value;
      const password = document.getElementById('password').value;

      // Appel de la fonction loginUser définie plus bas
      await loginUser(email, password);
    });
  }
});

// Fonction qui envoie la requête AJAX au serveur
async function loginUser(email, password) {
  try {
    // Envoie une requête POST au serveur avec l'email et le mot de passe
    const response = await fetch('http://127.0.0.1:5000/api/v1/auth/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json' // On dit au serveur qu'on envoie du JSON
      },
      body: JSON.stringify({ email, password }) // On transforme l'objet JS en JSON
    });

    // Si la réponse est bonne (statut HTTP 200–299)
    if (response.ok) {
      const data = await response.json(); // On récupère le corps de la réponse

      // On stocke le token dans un cookie (session)
      document.cookie = `token=${data.access_token}; path=/`;

      // On redirige vers la page principale
      window.location.href = 'index.html';
    } else {
      // Si la réponse est mauvaise, on affiche un message d’erreur
      alert('Login failed: ' + response.statusText);
    }
  } catch (error) {
    // Si une erreur se produit pendant la requête (ex : serveur injoignable)
    console.error('Erreur de connexion:', error);
    alert('Erreur lors de la connexion. Veuillez réessayer.');
  }
}

// ✅ Fonction pour récupérer un cookie par nom
function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}

function checkAuthentication() {
  const token = getCookie('token');
  const loginLink = document.getElementById('login-link');
  const addReviewSection = document.getElementById('add-review');

  if (loginLink) {
    loginLink.style.display = token ? 'none' : 'block';
  }

  if (addReviewSection) {
    addReviewSection.style.display = token ? 'block' : 'none';
  }

  const placeId = getPlaceIdFromURL();
  if (placeId) {
    fetchPlaceDetails(token, placeId);
  } else {
    fetchPlaces(token);
  }
}

let allPlaces = [];
// ✅ Récupère les lieux depuis l’API
async function fetchPlaces(token) {
  try {
    const response = await fetch('http://127.0.0.1:5000/api/v1/places/', {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    });

    if (response.ok) {
      const places = await response.json();
      displayPlaces(places);
    } else {
      console.error('Erreur lors de la récupération des lieux');
    }
  } catch (error) {
    console.error('Erreur réseau :', error);
  }
}

// ✅ Affiche les lieux dans #places-list
function displayPlaces(places) {
  const placesList = document.getElementById('places-list');
  placesList.innerHTML = ''; // Vide avant d’afficher

  places.forEach(place => {
    const placeElement = document.createElement('div');
    placeElement.classList.add('place-card');

    placeElement.innerHTML = `
      <h3>${place.name}</h3>
      <p>${place.description}</p>
      <p><strong>Lieu:</strong> ${place.location}</p>
      <p><strong>Prix:</strong> ${place.price} €</p>
      `;

    placesList.appendChild(placeElement);
  });
}

// ✅ Filtre les lieux en fonction du prix sélectionné
document.getElementById('price-filter').addEventListener('change', (event) => {
  const selectedValue = event.target.value;
  const maxPrice = selectedValue === 'All' ? Infinity : parseFloat(selectedValue);

  const filteredPlaces = allPlaces.filter(place => place.price <= maxPrice);
  displayPlaces(filteredPlaces);
});

// ✅ Exécution au chargement de la page

// ✅ Récupère un cookie par nom
function getCookie(name) {
  const cookieValue = document.cookie
    .split("; ")
    .find((row) => row.startsWith(name))
    ?.split("=")[1];
  return cookieValue;
}

// ✅ Récupère l’ID du lieu à partir de l’URL (?id=123)
function getPlaceIdFromURL() {
  const params = new URLSearchParams(window.location.search);
  return params.get('id') || null; // retourne null si aucun id n'est trouvé
}

// ✅ Vérifie si l’utilisateur est connecté + lance la récupération du lieu
function checkAuthentication() {
  const token = getCookie('token');
  const placeId = getPlaceIdFromURL();

  const addReviewSection = document.getElementById('add-review');
  if (addReviewSection) {
    addReviewSection.style.display = token ? 'block' : 'none';
  } 

  }

  if (placeId) {
    fetchPlaceDetails(token, placeId);
  } else {
    fetchPlaces(token);
  }

// ✅ Récupère les détails du lieu via l’API
async function fetchPlaceDetails(token, placeId) {
  try {
    const response = await fetch(`http://127.0.0.1:5000/api/v1/places/${placeId}`, {
      headers: token ? { 'Authorization': `Bearer ${token}` } : {}
    });

    if (response.ok) {
      const place = await response.json();
      displayPlaceDetails(place);
    } else {
      console.error('Erreur lors du chargement du lieu');
    }
  } catch (error) {
    console.error('Erreur réseau :', error);
  }
}

// ✅ Affiche les détails du lieu
function displayPlaceDetails(place) {
  const detailsSection = document.getElementById('place-details');
  const reviewsSection = document.getElementById('reviews');

  detailsSection.innerHTML = `
    <h1>${place.name}</h1>
    <p>${place.description}</p>
    <p><strong>Prix:</strong> ${place.price} €</p>
    <p><strong>Localisation:</strong> ${place.location}</p>
    <p><strong>Équipements:</strong> ${place.amenities.join(', ')}</p>
  `;

  reviewsSection.innerHTML = '<h2>Commentaires</h2>';
  place.reviews.forEach(review => {
    const reviewEl = document.createElement('div');
    reviewEl.classList.add('review');
    reviewEl.innerHTML = `<p>${review.text}</p>`;
    reviewsSection.appendChild(reviewEl);
  });
}