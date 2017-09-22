import API from '@/constants/index'
import Vue from 'vue'

export default {
  fetchLists () {
    return Vue.http.get(`${API.API_DOMAIN}${API.API_URL}lists`)
  }
}
