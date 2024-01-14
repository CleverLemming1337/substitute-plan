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
    this.data = JSON.stringify(http.getData("https://shiny-winner-4j67gj6j642jqxj-8000.app.github.dev/subst/class/7a"))
  }

  nav(url: string) {
    this.router.navigateByUrl(url);
  }
}
