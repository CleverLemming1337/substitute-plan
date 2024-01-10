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
  constructor(private http: HttpService, private router: Router) { 
    http.getData("http://localhost:8000/subst/class/7a").subscribe((response) => {
      alert(response);
    });
  }

  nav(url: string) {
    this.router.navigateByUrl(url);
  }
}
