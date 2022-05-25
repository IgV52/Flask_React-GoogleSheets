function TableData(props) {

    const { rows } = props

    if (!rows || rows.length === 0) return <p>Нет данных.</p>

    return (
        <div>
            <table>
                <thead>
                    <tr>
                    <th scope="col">№</th>
                    <th scope="col">заказ №</th>
                    <th scope="col">стоимость,$</th>
                    <th scope="col">срок поставки</th>
                    <th scope="col">стоимость в рублях</th>
                    </tr>
                </thead>
                <tbody>
                    {
                        rows.map((rows) =>
                            <tr key={rows.id}>
                                <td>{rows.id}</td>
                                <td>{rows.number_order}</td>
                                <td>{rows.price_by_usd}</td>
                                <td>{rows.delivery_date}</td>
                                <td>{rows.price_by_rub}</td>
                            </tr>
                        )
                    }
                </tbody>
            </table>
      </div>
    )
}

export default TableData