function WriteTimeToPay(next_payment_date)
{
    var config = GetConfig();
    config.next_payment_date = next_payment_date;
    WriteJSON(config);
}

function WriteJSON(new_json)
{
    fs.writeFile('user.json', data, (err) => {
        if (err) {
            throw err;
        }
        console.log("JSON data is saved.");
    });
}

function GetConfig()
{
    var fs=require('fs');

    var data=fs.readFileSync('config.json', 'utf8');
    data = data.toString('utf-8');
    data=JSON.parse(data);
    data.next_payment_date=new Date(data.next_payment_date);

    return data
}

function IsTimeToPay()
{
    return Date.now() < GetConfig().next_payment_date
}
console.log(GetConfig());
console.log(IsTimeToPay());