{
  const syms = [
    '.',
    '<',
    '>',
    'x',
    '-',
    'o',
  ]

  Vue.component('bullet-input', {
    name: 'bullet-input',
    data() {
      return {
        syms,
        editing: false,
      }
    },
    props: {
      bullet: Object,
    },
    methods: {
      changeSym(arrow, event) {
        event.preventDefault()
        const count = this.syms.length
        const index = (this.syms.indexOf(this.bullet.sym) + arrow + count) % count
        this.bullet.sym = this.syms[index]
      },
      submit() {
        if (!this.bullet.content) return
        if (!this.bullet.sym || this.bullet.sym === '?') this.bullet.sym = '-'
        this.$emit('submit', this.bullet)
      },
      handleFocus(bool) {
        if (!bool) this.submit()
        if (!bool && !this.bullet.content && this.bullet.sym === '?') return
        this.editing = bool
      },
      handleChange() {
        this.$nextTick(() => {
          const [matched, sym] = this.bullet.content.match(/^(\S+)\s/) || []
          if (!sym || this.syms.indexOf(sym) < 0) return
          this.bullet.sym = sym
          this.bullet.content = this.bullet.content.slice(matched.length)
        })
      },
      handleDelete() {
        if (this.bullet.content) return
        this.bullet.sym = ''
      }
    },
    mounted() {
      if (!this.bullet.content) {
        this.editing = true
      }
    },
    template: `
      <div class="bullet">
        <span class="bullet-sym" @keydown>{{ bullet.sym }}</span>
        <input class="bullet-input" type="text" v-model="bullet.content"
          :class="{ editing: editing }"
          @focus="handleFocus(true)"
          @blur="handleFocus(false)"
          @keyup="handleChange"
          @keydown.delete="handleDelete"
          @keydown.up="changeSym(-1, $event)"
          @keydown.down="changeSym(1, $event)"
          @keydown.enter="submit">
      </div>
    `
  })
}
