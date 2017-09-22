import MainHeader from '@/components/includes/header/Header'
import ListDetail from '@/components/lists/ListDetail'

export default function listRoutes (argument) {
  return [
    {
      path: '/list/:list_id',
      name: 'ListDetail',
      components: {
        header: MainHeader,
        main: ListDetail
      }
    }
  ]
}
