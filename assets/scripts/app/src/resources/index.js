import API from '@/constants/index'
import Vue from 'vue'

const apiRoute = `${API.API_DOMAIN}${API.API_URL}`

export default {
  fetchLists () {
    return Vue.http.get(`${apiRoute}lists`)
  },
  fetchListDetails (id) {
    return Vue.http.get(`${apiRoute}lists/${id}`)
  }
}
