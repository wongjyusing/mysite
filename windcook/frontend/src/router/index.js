import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import About from '@/components/About'
import BlogList from '@/components/BlogList'
import TagList from '@/components/TagList'
import BlogDetail from '@/components/BlogDetail'

import BlogTagList from '@/components/BlogTagList'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
  },
  {
    path: '/blogs',
    name: 'BlogList',
    component: BlogList
},
{
  path: '/about',
  name: 'About',
  component: About
},
{
  path: '/tagssss',
  name: 'TagList',
  component: TagList
},{
  path: '/detail/:slug',
  name: 'BlogDetail',
  component: BlogDetail
},{
  path: '/tags/:slug',
  name: 'BlogTagList',
  component: BlogTagList
},
  ]
})