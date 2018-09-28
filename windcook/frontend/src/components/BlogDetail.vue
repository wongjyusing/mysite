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




                </div>
            </div><!--col-xs-12 col-sm-9-->
            <div class="hidden-xs col-sm-3 site-me">
                <div class="panel panel-default">
                    <div class="panel-heading tags-title">
                        <h4>目录</h4>
                    </div>
                    <div v-html='toc'>

                    </div>
                </div><!--panel panel-default-->



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
      toc:''
    }
},mounted () {

        this.blog_slug = this.$route.params.slug;
        //Vue.prototype.$axios = axios,
        axios
          .get('http://127.0.0.1:8000/api/detail/' + this.blog_slug )
          .then(response => (this.blog = response.data.blog,
                            this.toc = response.data.blog.toc
                ))
      },

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/* =Base
-------------------------------------------------------------- */
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
</style>
