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
        hover: false,
      }
    },
    props: {
      bullet: Object,
      readonly: Boolean,
    },
    methods: {
      changeSym(arrow, event) {
        if (event) event.preventDefault()
        if (this.readonly) return
        const count = this.syms.length
        const index = (this.syms.indexOf(this.bullet.sym) + arrow + count) % count
        this.bullet.sym = this.syms[index]
      },
      handleClickSym() {
        changeSym(1)
        this.submit()
      },
      submit() {
        if (this.readonly) return
        if (!this.bullet.content) return
        if (!this.bullet.sym || this.bullet.sym === '?') this.bullet.sym = '-'
        this.$emit('submit', this.bullet)
        this.editing = false
      },
      focus() {
        this.$refs.input.focus()
      },
      handleEnter() {
        this.$refs.input.blur()
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
        if (this.bullet.sym === '?' && this.bullet.id) {
          this.delete()
          return
        }
        this.bullet.sym = '?'
      },
      handleMousehover(bool) {
        if (this.readonly) {
          this.hover = false
          return
        }
        this.hover = bool
      },
      delete() {
        this.$emit('delete', this.bullet)
      },
    },
    mounted() {
      if (!this.bullet.content) {
        this.editing = true
      }
    },
    template: `
      <div class="bullet">
        <span class="bullet-sym" @click="handleClickSym()">{{ bullet.sym }}</span>
        <input ref="input" class="bullet-input" type="text" v-model="bullet.content"
          :class="{ editing: editing }"
          :readonly="readonly"
          @focus="handleFocus(true)"
          @blur="handleFocus(false)"
          @keyup="handleChange"
          @keydown.delete="handleDelete"
          @keydown.up="changeSym(-1, $event)"
          @keydown.down="changeSym(1, $event)"
          @keydown.enter="handleEnter">
        <button v-if="hover" class="bullet-del">&times;</button>
      </div>
    `
  })
}
