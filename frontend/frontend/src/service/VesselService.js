import http from "../http-common";


export default class VesselService {

	getVessels() {
		return http.get("/vessels/");
    }

}
