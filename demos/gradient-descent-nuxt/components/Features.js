export default {
  name: 'Features',

  props: {
    x: {
      type: Array,
      required: true
    },

    y: {
      type: Array,
      required: true
    }
  },

  render () {
    return (
      <table>
        <thead>
          <tr>
            <th>x</th>
            <th>y</th>
          </tr>
        </thead>
        <tbody>
          {this.x.map((x, idx) =>
            <tr key={idx}>
              <td>{this.x[idx]}</td>
              <td>{this.y[idx]}</td>
            </tr>
          )}
        </tbody>
      </table>
    )
  }
}
