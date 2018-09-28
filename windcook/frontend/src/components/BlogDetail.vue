<template>
    <div class="container">
        <div class="row">
            <div class="col-xs-12 col-sm-9">
                <div class="panel panel-default">
                    <div class="panel-heading site-list-title">
                        <h4>{{ blog.title }}</h4>
                    </div>

                    <div class="content-data">
                    创建时间：<span class="max-len">{{ blog.created_time}}</span>&nbsp&nbsp&nbsp作者:{{ blog.author}}

                </div>
                    <br>
                    <div class="content-style" v-html="blog.body"></div>



                    <br>
                    <hr>
                    <div class="next-or-pre">
                        <nav aria-label="...">
                              <ul class="pager">

                                  <li class="previous disabled" v-if='previous.title === "现在阁下浏览的是第一篇文章"' key='pre_pages'><a href="javascript:volid(0);">现在阁下浏览的是第一篇文章</a></li>
                                  <li v-else class="previous" key='pre_pages'><router-link :to="{ name: 'BlogDetail', params: {slug:previous.slug} }">上一篇：《{{previous.title}}》</router-link></li>

                                <li class="next disabled" v-if='next_page.title === "现在阁下浏览到最后一篇了"' key='next_pages'><a href="javascript:volid(0);">现在阁下浏览到最后一篇了</a></li>

                                <li v-else class="next" key='next_pages'><router-link :to="{ name: 'BlogDetail', params: {slug:next_page.slug} }">下一篇《{{next_page.title}}》</router-link></li>
                              </ul>
                            </nav>
                    </div>
                </div>
            </div><!--col-xs-12 col-sm-9-->
            <div class="hidden-xs col-sm-3 ">

                <div class="site-me-widget-first-toc site-me">
                        <h4 class="title">目录</h4>
                        <hr>
                        <div v-html='toc'>

                        </div>
                    </div>




            </div><!-- hidden-xs col-sm-3 site-me -->
        </div><!-- row -->
        <router-view/>
    </div><!-- container -->

</template>

<script>
import axios from 'axios'

export default {

  name: 'BlogDetail',
  data () {
    return {
      blog: '',
      toc:'',
      next_page:'',
      previous:'',
    }
},mounted () {
        this.getSlug(this.$route.params.slug);
    },

        beforeRouteUpdate(to, from, next) {
        this.getSlug(to.params.slug);
           next();
      },
      methods: {
        getSlug(slug) {
            axios
              .get('http://127.0.0.1:8000/api/detail/' + slug )
              .then(response => (this.blog = response.data.blog,
                                this.toc = response.data.blog.toc,
                                this.next_page = response.data.next,
                                this.previous = response.data.previous
                    ))
         }
     }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/* =Base
-------------------------------------------------------------- */
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

.content-style{
    margin: 10px 10px 10px 10px;
}


.content-data{
    text-align: center;
    margin-top: 10px;
}
.max-len{
    -webkit-line-clamp: 10;
}
.site-tags{

    text-align: center;
}

.blog-list-tag li{
    float: left;
    list-style:none;
}
.next-or-pre{
    margin-left: 10px;
    margin-right: 10px;
}
.site-me{
    position: fixed;
    float: right;

}
div.site-me-widget-first-toc{

  background: #f5f5f5;
padding: 21px 30px;
position:fixed;
}

div.site-me-widget-first-toc h4{
    text-align: center;
}

</style>
