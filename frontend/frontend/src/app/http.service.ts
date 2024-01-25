import { Injectable } from '@angular/core';
import axios from 'axios';

@Injectable({
  providedIn: 'root'
})
export class HttpService {
  constructor() { }
  getData(url: any) {
    return axios.get(url, {
      headers: {
        
      }
    });
  }
  
}
