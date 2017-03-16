{
  /* global buildRecords */
  const records = buildRecords()
  const initRecord = () => ({ sym: '?', content: '' })
  const Main = {
    data() {
      return {
        bullets: records.getLocalBullets(),
        editingBullet: initRecord()
      }
    },
    mounted() {
    },
    methods: {
      addBullet(record) {
        const updated = records.addBullet(record)
        this.bullets = updated
        this.editingBullet = initRecord()
      },
      setBullet(record) {
        const updated = records.setBullet(record)
        this.bullelts = updated
      },
    },
    template: `
      <section>
        <h1>One Shot Demo: Bullet Component</h1>
        <bullet-input v-for="bullet of bullets" :key="bullets.id" :bullet="bullet" @submit="setBullet"></bullet-input>
        <bullet-input :bullet="editingBullet" @submit="addBullet"></bullet-input>
      </section>
    `,
  }


  const Ctor = Vue.extend(Main)
  new Ctor().$mount('#app')
}
