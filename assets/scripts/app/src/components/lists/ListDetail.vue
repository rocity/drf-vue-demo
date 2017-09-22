<template>
  <div class="container">
    <h1>List Detail</h1>
    <h3>{{ list.title }}</h3>
    <hr>
    <h3>Items</h3>
    <ul>
      <li v-for='item in list.items'>{{ item.content }}</li>
    </ul>
  </div>
</template>

<script>
  import resources from '@/resources'

  export default {
    data () {
      return {
        list: {}
      }
    },
    created () {
      resources.fetchListDetails(this.$route.params.list_id).then(response => {
        console.info('response--->>>', response.body)
        this.list = response.body
      })
    }
  }

</script>
