<template>
    <div class="container">
        <div class="row">
            <div class="col-xs-12 col-sm-9">
                <div class="panel panel-default">
                <div class="panel-heading site-list-title">
                    <h4>教程列表</h4>
                </div>
                    <div class="">
                        <table class="table table-bordered table-hover site-blog-table">
                            <thead>
                                <tr>
                                    <th>标题</th>

                                    <th>状态</th>
                                </tr>
                            </thead>
                            <tbody>

                                    <tr v-for='book in gitbook' >

                                        <th scope="row"><a v-bind:href="book.link" target="_blank" >{{book.name}}</a></th>

                                        <td>{{ book.book_status }}</td>


                                    </tr>
                            </tbody>
                        </table>
                    </div>


                </div>
            </div><!--col-xs-12 col-sm-9-->
            <div class="hidden-xs col-sm-3 site-me">
                <div class="panel panel-default">
                    <div class="panel-heading tags-title">
                        <h4>个人空间</h4>
                    </div>
                    <ul v-for='naw in space_link'  class="list-group">

                        <li class="list-group-item"><a v-bind:href="naw.link" target="_blank">{{naw.name}}</a></li>
                    </ul>
                </div><!--panel panel-default-->

                <div class="panel panel-default">
                    <div class="panel-heading tags-title">
                        <h4>标签</h4>
                    </div>
                    <ul v-for='naw in toolbox_tags'  class="list-group">

                        <li class="list-group-item"><router-link :to="{ name: 'BlogTagList', params: {'slug':naw.slug} }">{{ naw.name}}</router-link></li>
                    </ul>

                </div><!--panel panel-default-->

                <div class="panel panel-default">
                    <div class="panel-heading tags-title">
                        <h4>书籍推荐</h4>
                    </div>
                    <ul v-for='naw in book_link'  class="list-group">

                        <li class="list-group-item"><a v-bind:href="naw.link" target="_blank">{{naw.name}}</a></li>
                    </ul>
                </div><!--panel panel-default-->

                <div class="panel panel-default">
                    <div class="panel-heading tags-title">
                        <h4>友情链接</h4>
                    </div>
                    <ul v-for='naw in friend_link'  class="list-group">

                        <li class="list-group-item"><a v-bind:href="naw.link" target="_blank">{{naw.name}}</a></li>
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
      gitbook: '',
      toolbox_tags:'',
      pages:null,
      now_page:null,
      friend_link:null,
      space_link:'',
      book_link:'',
      //page_list:(1,this.pages)
    }
},mounted () {

        //Vue.prototype.$axios = axios,
        this.getPage(this.$route.params.page);
        },


      methods: {
        getPage(page) {
            axios
              .get('http://127.0.0.1:8000/api/book/')
              .then(response => (this.gitbook = response.data.gitbook,

                                this.friend_link = response.data.friend_link,
                                this.space_link = response.data.space_link,
                                this.book_link = response.data.book_link,
                                this.toolbox_tags = response.data.toolbox_tags
                    ));
         }
     }
      /*
      beforeRouteUpdate(to,from,next){
          this.blog_slug = this.to.$route.params.slug;
          next();}*/
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
a{
    color: #111;
}
a:link {text-decoration:none;}

a:visited {text-decoration:none;}
a:hover { text-decoration:none;}
ul {
    list-style-type:none;
}
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
.page-card{
    text-align: center;
}
</style>
