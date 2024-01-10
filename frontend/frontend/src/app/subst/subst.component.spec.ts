import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SubstComponent } from './subst.component';

describe('SubstComponent', () => {
  let component: SubstComponent;
  let fixture: ComponentFixture<SubstComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SubstComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(SubstComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
