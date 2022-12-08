import BaseAPI from './BaseAPI';

class TankDataAPI extends BaseAPI {
    constructor() {
        super("/data");
    }

    async getAll(min_date="", max_date="") {
        if (min_date === "" && max_date === "") {
            return this.get("");
        } else if (min_date === "") {
            return this.get(`?max_date=${max_date}`);
        } else if (max_date === "") {
            return this.get(`?min_date=${min_date}`);
        } else {
            console.log(`?min_date=${min_date}&max_date=${max_date}`);
            return this.get(`?min_date=${min_date}&max_date=${max_date}`);
        }
    }
}

export default new TankDataAPI();