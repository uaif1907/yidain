<template>
  <div class="recommend">
    <div class="bidbox">
        <div class="top">
            
        </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'recommend',
  components: {
    HelloWorld
  }
}
</script>
<style>
    .bigbox{
        width:100%;
        height:100%;
    }
    .top{
        width:550px;
        height: 200px;
        margin: auto;
        background: url('../../../assets/recommend-img/topback.png') no-repeat;
    }
</style>