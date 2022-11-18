<template>
  <div class="">
    <p>L18N {{ $t('language') }}</p>
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

<!-- 
<NuxtLink :to="localePath('index')">{{ $t('home') }}</NuxtLink>
<NuxtLink :to="localePath('/')">{{ $t('home') }}</NuxtLink>
<NuxtLink :to="localePath('index', 'en')">Homepage in English</NuxtLink>
<NuxtLink :to="localePath('/user/profile')">Route by path to: {{ $t('profile') }}</NuxtLink>
<NuxtLink :to="localePath('user-profile')">Route by name to: {{ $t('profile') }}</NuxtLink>
<NuxtLink :to="localePath({ name: 'category-slug', params: { slug: category.slug } })">
-->
