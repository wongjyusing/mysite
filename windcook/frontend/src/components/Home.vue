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
                    <div class="content-style" v-html="blog.body"></div>




                </div>
            </div><!--col-xs-12 col-sm-9-->
            <div class="hidden-xs col-sm-3 site-me">
                <div class="panel panel-default">
                    <div class="panel-heading tags-title">
                        <h4>个人空间</h4>
                    </div>
                    <ul v-for='naw in space_link'  class="list-group">

                        <li class="list-group-item"><a v-bind:href="naw.link">{{naw.name}}</a></li>
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

                        <li class="list-group-item"><a v-bind:href="naw.link">{{naw.name}}</a></li>
                    </ul>
                </div><!--panel panel-default-->

                <div class="panel panel-default">
                    <div class="panel-heading tags-title">
                        <h4>友情链接</h4>
                    </div>
                    <ul v-for='naw in friend_link'  class="list-group">

                        <li class="list-group-item"><a v-bind:href="naw.link">{{naw.name}}</a></li>
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

  name: 'Home',
  data () {
    return {
      blog: '',
      toolbox_tags:'',
      friend_link:null,
      space_link:'',
      book_link:'',

    }
},mounted () {
        //Vue.prototype.$axios = axios,
        axios
          .get('http://127.0.0.1:8000/api/home')
          .then(response => (this.blog = response.data.home[0],
              this.friend_link = response.data.friend_link,
              this.space_link = response.data.space_link,
              this.book_link = response.data.book_link,
              this.toolbox_tags = response.data.toolbox_tags

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

.blog-list-tag li{
    float: left;
    list-style:none;
}
.content-data{
    text-align: center;
}
.content-style{
    margin: 10px 10px 10px 10px;
}
.max-len{
    -webkit-line-clamp: 10;
}
</style>
