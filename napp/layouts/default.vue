<template>

  <div class="bg-gradient-to-r from-gray-200 to-gray-100 text-gray-700">
    
    <div class="">

      <div class="container mx-auto">

        <transition name="fade" mode="out-in">
          <Nuxt id="page" />
        </transition>

      </div>      
    </div>


  </div>
     
  
</template>
    
<script>

  export default {
    // head: {
    //   title: "Nuxt.js with TailwindCSS",
    //   meta: [
    //       { charset: "utf-8" },
    //       { name: "viewport", content: "width=device-width, initial-scale=1" },
    //       {
    //           hid: "description",
    //           name: "description",
    //           content: "Nuxt.js with TailwindCSS example",
    //       },
    //   ],
    //   link: [{ rel: "icon", type: "image/x-icon", href: "/favicon.png" }],
    // },
    components: {

    },
    data() {
      return {
        dataset: true,
      }
    },
  //   methods: {
  //     addTodo (e) {
  //       this.$store.commit('todos/add', e.target.value)
  //       e.target.value = ''
  //     },
  //     ...mapMutations({
  //       toggle: 'todos/toggle'
  //     })
  //   },
  //   computed: {
  //     ...mapState({
  //       cartModal: (state) => state.modules.cart.cartModal,
  //       shopModal: (state) => state.shopModal
  //     }),
  //   },
  };
</script>