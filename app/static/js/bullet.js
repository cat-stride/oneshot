function buildRecords() {
  const BULLET_RECORDS = 'BULLET_RECORDS'
  const BULLET_INDEX = 'BULLET_INDEX'

  function parseJSON(raw) {
    try {
      return JSON.parse(raw)
    } catch (e) {
      return null
    }
  }

  function getLocalCount() {
    return +localStorage.getItem(BULLET_INDEX)
  }

  function incLocalCount() {
    const count = getLocalCount() + 1
    localStorage.setItem(BULLET_INDEX, count)
    return count
  }

  function getLocalBullets() {
    const raw = localStorage.getItem(BULLET_RECORDS)
    return parseJSON(raw) || []
  }

  function saveLocalBullets(bullets) {
    localStorage.setItem(BULLET_RECORDS, JSON.stringify(bullets))
    return bullets
  }

  function getBullet(id, bullets) {
    return (bullets || getLocalBullets()).find(bullet => bullet.id === id)
  }

  function addBullet({ sym, content }) {
    const bullets = getLocalBullets()
    const id = incLocalCount()
    bullets.push({ sym, content, id })
    saveLocalBullets(bullets)
    return bullets
  }

  function setBullet({ id, sym, content }) {
    const bullets = getLocalBullets()
    const bullet = getBullet(id, bullets)
    Object.assign(bullet, { sym, content })
    saveLocalBullets(bullets)
    return bullets
  }

  function removeBullet({ id }) {
    const bullets = getLocalBullets()
    const index = bullets.indexOf(getBullet(id, bullets))
    bullets.splice(index, 1)
    saveLocalBullets(bullets)
    return bullets
  }

  return {
    getLocalBullets,
    getBullet,
    addBullet,
    setBullet,
    removeBullet,
  }
}

// TESTING
if (!localStorage.getItem('BULLET_RECORDS')) {
  const raw = '[{"sym":">","content":"一个延期","id":2},{"sym":">","content":"又一个延期","id":3},{"sym":".","content":"这是今天的待办","id":4},{"sym":"x","content":"这是待办完成","id":5},{"sym":"o","content":"这是一个事件","id":6},{"sym":"-","content":"这是普通的笔记","id":7},{"sym":"x","content":"输入一条 bullet，回车或失去焦点时保存","id":8},{"sym":"x","content":"然后进入下一条 bullet 编辑","id":9},{"sym":"x","content":"正在编辑的状态要区分开","id":10},{"sym":"<","content":"删除今天先不做了","id":11},{"sym":"x","content":"第一个空格前的字符如果是符号，则放置为符号","id":12},{"sym":"x","content":"编辑状态按上下键可以快捷切换符号","id":13},{"sym":"<","content":"优化样式","id":14},{"sym":"-","content":"这样如何","id":15},{"sym":"o","content":"超出计划时长太多了，今天熬夜了","id":16}]'
  localStorage.setItem('BULLET_RECORDS', raw)
  localStorage.setItem('BULLET_INDEX', 16)
}
