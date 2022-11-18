<template>
  <div class="">
    <p>L18N</p>
    <nuxt-link :to="switchLocalePath('en')">English</nuxt-link>
    <nuxt-link :to="switchLocalePath('de')">Deutsch</nuxt-link>
    <nuxt-link :to="switchLocalePath('ru')">Русский</nuxt-link>
  </div>
</template>

<script>

export default {
  name: 'HeaderSection',
}
</script>

<!-- localePath({ name: 'category-slug', params: { slug: category.slug } } -->