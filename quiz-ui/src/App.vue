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
  background-color: black;
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
  max-width: 1200px;
  margin: 0 auto;
  padding: 1rem;
}

.logo {
  display: block;
  width: 20%;
  height: 100%;
}

nav ul {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
}

nav li {
  margin-left: 1rem;
}

nav a {
  color: #7cc4fb;
  text-decoration: none;
  font-weight: 600;
  font-size: 1.2rem;
  transition: color 0.2s ease-in-out;
}

nav a:hover {
  color: #8c4ad8;
}
.main-content {
  margin-top: 5rem;
}
</style>
