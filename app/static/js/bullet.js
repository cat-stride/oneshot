function buildRecords() {
  const BULLET_RECORDS = 'BULLET_RECORDS'
  const BULLET_INDEX = 'BULLET_INDEX'
  const API = '/api/bullets'
  const SYM_TO_STRING = {
    '.': 'today',
    '>': 'delay',
    '<': 'future',
    'x': 'done',
    '-': 'note',
    'o': 'event',
  }
  const STRING_TO_SYM = (() => {
    return Object.keys(SYM_TO_STRING).reduce((prev, current) => {
      prev[SYM_TO_STRING[current]] = current
      return prev
    }, {})
  })()

  function parseJSON(raw) {
    try {
      return JSON.parse(raw)
    } catch (e) {
      return null
    }
  }

  function parseRecordSyms(records) {
    return records.map(record => {
      record.sym = STRING_TO_SYM[record.type]
      // record.id = record.bid
      return record
    }).sort((a, b) => a.id > b.id)
  }

  function stringifyRecordSyms(records) {
    return records.map(record => {
      record.type = SYM_TO_STRING[record.sym]
      // record.bid = record.id
      return record
    })
  }

  async function getBullets() {
    const records = await fetch(API,{credentials: 'include'}).then(r => r.json())
    saveLocalBullets(parseRecordSyms(records))
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

  async function addBullet({ sym, content }) {
    const record = await fetch(API, {
      method: 'POST',
      body: JSON.stringify({ type: SYM_TO_STRING[sym], content: content }),
      credentials: 'include'
    }).then(r => r.json())
    const bullets = await getBullets()
    saveLocalBullets(bullets)
    return bullets
  }

  async function setBullet({ id, sym, content }) {
    const record = await fetch(`${API}/${id}`, {
      method: 'PUT',
      body: JSON.stringify({ type: SYM_TO_STRING[sym], content: content }),
      credentials: 'include'
    }).then(r => r.json())
    const bullets = await getBullets()
    saveLocalBullets(bullets)
    return bullets
  }

  async function removeBullet({ id }) {
    const record = await fetch(`${API}/${id}`, {
      method: 'DELETE',
      credentials: 'include'
    }).then(r => r.json())
    const bullets = await getBullets()
    saveLocalBullets(bullets)
    return bullets
  }

  return {
    getBullets,
    getBullet,
    addBullet,
    setBullet,
    removeBullet,
  }
}