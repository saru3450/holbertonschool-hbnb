/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

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
      const response = await fetch('https://your-api-url/login', {
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