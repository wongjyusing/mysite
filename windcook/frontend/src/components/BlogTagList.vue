<template>
    <div class="container">
        <div class="row">
            <div class="col-xs-12 col-sm-9">
                <div class="panel panel-default">
                <div class="panel-heading site-list-title">
                    <h4>{{blog_tag.name}}的博文列表</h4>
                </div>
                <div class="">
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

                                    <td class="blog-list-tag"><li v-for='tag in blog.blog_tag'><router-link :to="{ name: 'BlogTagList', params: {'slug':tag.slug,'page':1} }">{{ tag.name}}</router-link>,</li></td>
                                </tr>
                        </tbody>
                    </table>


                    </div>
                    <div class="page-card">
                        <nav aria-label="Page navigation">
                              <ul class="pagination">

                                    <li v-if='now_page ==1' key='pre_page' class="disabled">
                                        <span aria-hidden="true">&laquo;</span>
                                    </li>
                                    <li v-else key='pre_page'>
                                        <router-link aria-label="Previous" :to="{ name: 'BlogTagList', params: {'page':(now_page - 1)} }"><span aria-hidden="false">&laquo;</span></router-link>
                                    </li>


                                <li v-for='page in pages'>
                                    <router-link :to="{ name: 'BlogTagList', params: {'page':page} }">{{page}}</router-link>
                                </li>





                                <li v-if='now_page ==pages' key='next_page' class="disabled">
                                    <span aria-hidden="true">&raquo;</span>
                                </li>
                                <li v-else key='next_page'>
                                    <router-link aria-label="Next" :to="{ name: 'BlogTagList', params: {'page':(now_page - 1)} }"><span aria-hidden="false">&raquo;</span></router-link>
                                </li>

                              </ul>
                            </nav>
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

  name: 'BlogTagList',
  data () {
    return {
        blogs: '',
        pages:null,
        now_page:null,
        toolbox_tags:'',
        friend_link:null,
        space_link:'',
        book_link:'',
        blog_tag:'',
    }
},
mounted() {
           // 接受url参数slug
        this.getSlug(this.$route.params.slug,this.$route.params.page);
        },

        beforeRouteUpdate(to, from, next) {
            this.detail = this.getSlug(to.params.slug,to.params.page);
           next();
       },

        methods: {
          getSlug(slug,page) {
              axios
                .get('http://127.0.0.1:8000/api/tag/'+ slug + '/?page=' + page)
                .then(response => (this.blogs = response.data.blogs,
                    this.blog_tag = response.data.blog_tag,
                    this.pages = parseInt(response.data.page.page_count),
                    this.now_page = parseInt(response.data.page.now_page),
                    this.friend_link = response.data.friend_link,
                    this.space_link = response.data.space_link,
                    this.book_link = response.data.book_link,
                    this.toolbox_tags = response.data.toolbox_tags
                      ))
           }
       }
   };




/*mounted () {
        this.blog_slug = this.getSlug(this.$route.params.slug);
        //Vue.prototype.$axios = axios,
        beforeRouteUpdate (to, from, next) {
            this.blog_slug = this.getSlug(to.params.slug)
            next();

      }},

    methods:{
        getSlug(slug){
            axios
              .get('http://127.0.0.1:8000/api/tag/'+ slug)
              .then(response => (this.blogs = response.data.blogs
                    ))
        }
    },

}*/

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
