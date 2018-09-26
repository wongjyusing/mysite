<template>
    <div class="container">
        <div class="row">
            <div class="col-xs-12 col-sm-9">
                <div class="panel panel-default">
                <div class="panel-heading site-list-title">
                    <h4>博客列表</h4>
                </div>
                    <table class="table table-bordered table-hover site-blog-table">
                        <thead>
                            <tr>
                                <th>标题</th>
                                <th>时间</th>
                                <th>所属标签</th>
                            </tr>
                        </thead>
                        <tbody>

                                <tr v-for='blog in blogs' >

                                    <th scope="row"><router-link :to="{ name: 'BlogDetail', params: {'slug':blog.slug} }">{{ blog.title}}</router-link></th>
                                    <td>{{ blog.created_time.slice(0,10)}}</td>

                                    <td class="blog-list-tag"><li v-for='tag in blog.blog_tag'><router-link :to="{ name: 'BlogTagList', params: {'slug':tag.slug} }">{{ tag.name}}</router-link>,</li></td>
                                </tr>
                        </tbody>
                    </table>
                </div>
            </div><!--col-xs-12 col-sm-9-->
            <div class="hidden-xs col-sm-3 site-me">
                <div class="panel panel-default">
                    <div class="panel-heading tags-title">
                        <h4>个人空间</h4>
                    </div>
                    <ul class="list-group">
                        <li class="list-group-item">Cras justo odio</li>
                        <li class="list-group-item">Dapibus ac facilisis in</li>
                        <li class="list-group-item">Morbi leo risus</li>
                    </ul>
                </div><!--panel panel-default-->

                <div class="panel panel-default">
                    <div class="panel-heading tags-title">
                        <h4>标签</h4>
                    </div>
                    <div class="tags-cloud">
                        <li class="list-group-item">Cras justo odio</li>
                        <li class="list-group-item">Dapibus ac facilisis in</li>
                        <li class="list-group-item">Morbi leo risus</li>
                    </div>

                </div><!--panel panel-default-->

                <div class="panel panel-default">
                    <div class="panel-heading tags-title">
                        <h4>书籍推荐</h4>
                    </div>
                    <ul class="list-group">
                        <li class="list-group-item">Cras justo odio</li>
                        <li class="list-group-item">Dapibus ac facilisis in</li>

                    </ul>
                </div><!--panel panel-default-->

                <div class="panel panel-default">
                    <div class="panel-heading tags-title">
                        <h4>友情链接</h4>
                    </div>
                    <ul class="list-group">
                        <li class="list-group-item">Cras justo odio</li>
                        <li class="list-group-item">Dapibus ac facilisis in</li>
                        <li class="list-group-item">Morbi leo risus</li>
                        <li class="list-group-item">Porta ac consectetur ac</li>
                        <li class="list-group-item">Vestibulum at eros</li>
                    </ul>
                </div><!--panel panel-default-->

            </div><!-- hidden-xs col-sm-3 site-me -->
        </div><!-- row -->
        <router-view/>
    </div><!-- container -->


</template>

<script>
import axios from 'axios'

export default {

  name: 'BlogList',
  data () {
    return {
      blogs: '',
      markdown:'',
      toc:''
    }
},mounted () {

        //Vue.prototype.$axios = axios,
        axios
          .get('http://127.0.0.1:8000/api/')
          .then(response => (this.blogs = response.data.blogs
                ))
      },
      beforeRouteUpdate(to,from,next){
          this.blog_slug = this.to.$route.params.slug;
          next();}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.site-list-title{
    font-weight: bold;
    text-align: center;
}
.tags-title{
    text-align: center;
}
.blog-list-tag li{
    float: left;
    list-style:none;
}
</style>
