<template>
  <div class="about">
    <h1>About Us</h1>
    <div class="row">
      <div class="col-md-4">
        <div class="card">
          <img src="/src/assets/photos/hug.jpg" alt="Hugo" />
          <h3>Hugo</h3>
          <p class="pAbout">Co-Founder & CEO</p>
          <p class="pAbout">Hugo is passionate about empowering people to reach their full potential and achieve their goals. He brings a wealth of experience in business development and management to BrokenMinds.</p>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card">
          <img src="/src/assets/photos/val.jpg" alt="Valentin" />
          <h3>Valentin</h3>
          <p class="pAbout">Co-Founder & CMO</p>
          <p class="pAbout">Valentin is an experienced marketer with a talent for crafting compelling brand stories. She leads the marketing and branding efforts at BrokenMinds, ensuring that our message resonates with our target audience.</p>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card">
          <img src="/src/assets/photos/gab.jpg" alt="Gabriel" />
          <h3>Gabriel</h3>
          <p class="pAbout">Co-Founder & CTO</p>
          <p class="pAbout">Gabriel is a creative problem-solver with a passion for technology. He leads the development efforts at BrokenMinds, ensuring that our platform is robust, scalable, and user-friendly.</p>
        </div>
      </div>
    </div>
    <p class="pAbout">At BrokenMinds, we believe that everyone has the potential to achieve greatness. Our mission is to empower individuals to unlock their full potential by providing them with the tools, resources, and support they need to succeed.
    <br>Whether you're an entrepreneur, a student, a professional, or anyone looking to improve their life, BrokenMinds has something to offer. Join our community today and start your journey to greatness!</p>
    <div class="social-links">
        <a href="https://www.instagram.com/la_mushrooom/">
        <img src="/src/assets/icons/instagram.svg" alt="Instagram" />
      </a>
      <a href="https://github.com/Gabi201265/quiz-app">
        <img src="/src/assets/icons/github.svg" alt="Github" />
      </a>
    </div>
  </div>
</template>

<style>

.about {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 2rem;
  margin-top: 5rem;
  color: #FFFFFF;
}

h1 {
  font-size: 36px;
  margin-bottom: 30px;
}

.card {
  margin-bottom: 30px;
  padding: 20px;
  background-color: #FFFFFF;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.card img {
  display: block;
  margin: 0 auto 20px;
  border-radius: 50%;
  width: 150px;
  height: 150px;
  object-fit: cover;
}

.card h3 {
  font-size: 24px;
  margin-bottom: 10px;
}

.card p {
  margin-bottom: 20px;
  font-size: 14px;
  color: #4A4A4A;
  line-height: 1.5;
  text-align: left;
}

.pAbout {
  font-size: 16px;
  margin-bottom: 20px;
  text-align: center;
}

.social-links {
  fill: white;
  padding-top:2rem;
}
.social-links a {
  display: inline-block;
  width: 50px;
  height: 30px;
  margin: 0 20px;
}

.social-links a:hover {
  opacity: 0.7;
}

</style>
