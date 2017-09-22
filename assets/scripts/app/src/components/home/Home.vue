<template>
  <div>
    <h1>Lists</h1>

    <div v-for='list in lists' class="card">
      <div class="content" v-if='list'>
        <p class="title"><strong>{{ list.title }}</strong></p>
        <hr>
        <router-link :to="{name: 'ListDetail', params: {list_id: list.id}}">Details</router-link>
      </div>
    </div>
  </div>
</template>

<script>
  import resources from '@/resources'
  export default {
    data () {
      return {
        lists: []
      }
    },
    created () {
      resources.fetchLists().then(response => {
        this.lists = response.body.results
      })
    }
  }
</script>
