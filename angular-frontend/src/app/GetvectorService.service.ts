import { Injectable } from '@angular/core';
// import { Headers } from '@angular/http';

import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable()
export class GetvectorService {
    constructor(private http: HttpClient) {
        console.log('Vector service initialised...');
    }

    // http://express-backend/vectorfor/?word=
    getVector(word: string): Observable<any> {
        var res = this.http.get('http://localhost:5000/vectorfor/?word=' + word);
        console.log(res);
        return res
    }
}