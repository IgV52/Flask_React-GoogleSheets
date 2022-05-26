function TableData(props) {

    const { rows } = props

    if (!rows || rows.length === 0) return <p>Нет данных.</p>

    return (
        <div>
            <table>
                <thead>
                    <tr>
                    <th>№</th>
                    <th>заказ №</th>
                    <th>стоимость,$</th>
                    <th>срок поставки</th>
                    <th>стоимость в рублях</th>
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