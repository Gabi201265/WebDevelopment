<template>
  <div>
    <header>
      <div class="header-content">
        <img alt="Vue logo" class="logo" src="@/assets/logo.svg" />
        <nav>
          <ul>
            <li>
              <RouterLink to="/">Home</RouterLink>
            </li>
            <li>
              <RouterLink to="/admin">Admin</RouterLink>
            </li>
            <li>
              <RouterLink to="/about">About</RouterLink>
            </li>
          </ul>
        </nav>
      </div>
    </header>

    <main class="main-content">
      <RouterView />
    </main>
  </div>
</template>

<style scoped>
header {
  background-color: transparent;
  backdrop-filter: blur(5px);
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1;
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
}

.logo {
  padding-left: 0.5rem;
  display: block;
  width: 18%;
  height: 100%;
  max-height: 4rem;
}

nav ul {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
  padding-right: 3rem;
}

nav li {
  margin-left: 2.5rem;
  list-style: none;
}

nav a {
  color: aliceblue;
  text-decoration: none;
  font-size: 2rem;
  letter-spacing: 1px;
}

nav a:hover {
  background: linear-gradient(45deg, #7cc4fb, #8c4ad8);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

nav a::before {
  content: "";
  position: absolute;
  height: 5px;
  bottom: -1em;
  width: 0;
  border-radius: 50px;
  background: linear-gradient(45deg, #7cc4fb, #8c4ad8);
  transition: 0.5s;
}

nav a:hover::before {
  width: 100%;
}

@media (max-width: 768px) {
  .header-content {
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    padding: 0.5rem;
  }

  .logo {
    width: 40%;
    max-height: 2.5rem;
  }

  nav ul {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 0;
    margin-top: 1rem;
  }

  nav li {
    margin: 0 0.5rem;
  }
  nav a::before {
    bottom: -0.7em;
  }
}
</style>
