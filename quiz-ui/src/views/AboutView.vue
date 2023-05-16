<template>
  <div class="container about">
    <h1>About Us</h1>
    <div class="row">
      <div class="col-md-4">
        <div class="card">
          <img src="@/assets/photos/hug.jpg" alt="Hugo" />
          <h3>Hugo</h3>
          <p>Co-Founder & CEO</p>
          <p>Hugo is passionate about empowering people to reach their full potential and achieve their goals. He brings a wealth of experience in business development and management to BrokenMinds.</p>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card">
          <img src="@/assets/photos/val.jpg" alt="Valentin" />
          <h3>Valentin</h3>
          <p>Co-Founder & CMO</p>
          <p>Valentin is an experienced marketer with a talent for crafting compelling brand stories. She leads the marketing and branding efforts at BrokenMinds, ensuring that our message resonates with our target audience.</p>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card">
          <img src="@/assets/photos/gab.jpg" alt="Gabriel" />
          <h3>Gabriel</h3>
          <p>Co-Founder & CTO</p>
          <p>Gabriel is a creative problem-solver with a passion for technology. He leads the development efforts at BrokenMinds, ensuring that our platform is robust, scalable, and user-friendly.</p>
        </div>
      </div>
    </div>
    <p>At BrokenMinds, we believe that everyone has the potential to achieve greatness. Our mission is to empower individuals to unlock their full potential by providing them with the tools, resources, and support they need to succeed.</p>
    <p>Whether you're an entrepreneur, a student, a professional, or anyone looking to improve their life, BrokenMinds has something to offer. Join our community today and start your journey to greatness !</p>
    <div class="social-links">
      <a href="https://www.instagram.com/la_mushrooom/">
        <img src="@/assets/icons/instagram.svg" alt="Instagram" />
      </a>
      <a href="https://github.com/Gabi201265/quiz-app">
        <img src="@/assets/icons/github.svg" alt="Github" />
      </a>
    </div>
  </div>
</template>

<style scoped>
.about {
  padding-top: 30px;
  text-align: center;
  margin-left: 50%;
}

.card {
  margin-bottom: 1.5rem;
  padding: 1.5rem;
  background-color: var(--color-light);
  border-radius: 0.25rem;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.card img {
  display: block;
  margin: 0 auto 1.5rem;
  border-radius: 50%;
  max-width: 150px;
  max-height: 150px;
  object-fit: cover;
}

.card h3 {
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
}

.card p {
  margin-bottom: 1rem;
  font-size: 0.875rem;
  color: var(--color-text-secondary);
  line-height: 1.5;
  justify-content:left;
}
.social-links a {
  display: inline-block;
  width: 30px;
  height: 30px;
  margin: 0 10px;
}

.social-links a:hover {
  color:transparent;
}

</style>
