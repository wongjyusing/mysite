<template>
  <div id="app">
      <header class="site-header">
          <div class="site-branding">
              <h1 class="site-title"><a href="/">花若盛開 蝴蝶自來</a></h1>
              <div class="site-introduction">这是我用Django2.1和Vue.js2.0搭建的博客</div>
          </div>
          <nav class="main-navigation">
          <div class="container">
              <div class="row">
                  <div class="col-sm-12">
                      <ul class="menu">
                          <li exact><router-link :to="{ name: 'Home', params: {} }" exact>首页</router-link></li>
                          <li exact><router-link :to="{ name: 'BlogList', params: {} }">博客列表</router-link></li>
                          <li exact><router-link :to="{ name: 'TagList', params: {} }">标签</router-link></li>
                          <li exact><router-link :to="{ name: 'About', params: {} }">关于</router-link></li>
                      </ul>
                  </div>
              </div>
          </div>
          </nav>
      </header>
      <router-view/>

      <footer>
        <div class="diy-card">
            <p>Copyright © 2018 Sing. Powered by Django.</p>
            <p>粤ICP备18079962号</p>
        </div>
    </footer>

  </div>

</template>

<script>

export default {
  name: 'App',


}
</script>

<style>
#app {

}
/* =Base
-------------------------------------------------------------- */

.router-link-active {
    border-bottom: 2px solid #e67e22;
    margin-bottom: -2px;
       }




a{
    color: #111
}
a:link {text-decoration:none;}

a:visited {text-decoration:none;}
a:hover { text-decoration:none;}

.home-template .main-header {
  padding-top: 62px;
  padding-bottom: 62px;
  background-repeat: no-repeat;
  background-position: center 20%;
  -webkit-background-size: cover;
          background-size: cover;
}
/* =Header
-------------------------------------------------------------- */


.site-header{

    margin-bottom: 0px;
	text-align: center;
}

.site-branding{
    margin: 0 auto;
	padding: 12px 0 24px;

	background-color: #f6911e;
	-webkit-background-image: -webkit-linear-gradient(90deg, #f6911e, #febd36);
	background-image: linear-gradient(90deg, #f6911e, #febd36)
}

.site-title{
    margin-top: 20px;
    margin-bottom: 2px;
    font-weight: bold;
}
.site-title a:hover {
	color: #555;
}
.site-introduction {
	color: #555;
	font-size: 15px;
}

/* =Navbar
-------------------------------------------------------------- */
.main-navigation {
  text-align: center;
  background: #ffffff;
  border-top: 1px solid #ebebeb;
  margin-bottom: 10px;
  border-bottom: 2px solid #e1e1e1;
}
.main-navigation .menu {
  padding: 0;
  margin: 0;
}
.main-navigation .menu li {
  list-style: none;
  display: inline-block;
  position: relative;
}
/* cheak  */
.main-navigation .menu li.nav-current {
  border-bottom: 2px solid #e67e22;
  margin-bottom: -2px;
}

.main-navigation .menu li a {
  color: #505050;
  line-height: 4em;
  display: block;
  padding: 0 21px;
}
.main-navigation .menu li:hover > a {
  color: #e67e22;
  text-decoration: none;
}
.main-navigation .menu li ul {
  visibility: hidden;
  background: #ececec;
  text-align: left;
  padding: 7px 0px;
  margin: 0;
  position: absolute;
  left: 0;
  top: 120%;
  width: 200px;
  z-index: 999;
  opacity: 0;
  filter: alpha(opacity=0);
  -webkit-transition: all 0.2s ease;
  -o-transition: all 0.2s ease;
  transition: all 0.2s ease;
}
.main-navigation .menu li ul li {
  display: block;
  margin: 0;
}
.main-navigation .menu li ul li a {
  line-height: 2.5em;
  color: #505050;
}
.main-navigation .menu li ul:hover > a {
  color: #e67e22;
}
.main-navigation .menu li:hover ul {
  visibility: visible;
  opacity: 1;
  filter: alpha(opacity=100);
  top: 100%;
}



div.diy-card{
    padding-top: 30px;
}
div.diy-card p{
  text-align: center;
}
</style>
