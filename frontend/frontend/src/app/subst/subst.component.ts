import { Component } from '@angular/core';
import { HttpService } from '../http.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-subst',
  standalone: true,
  templateUrl: './subst.component.html',
  styleUrls: ['./subst.component.scss']
})
export class SubstComponent {
  data: any;
  constructor(private http: HttpService, private router: Router) { 
    this.data = JSON.stringify(http.getData("http://localhost:8001/subst"))
    alert(this.data)
  }

  nav(url: string) {
    this.router.navigateByUrl(url);
  }
}